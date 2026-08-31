# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 478
- HTTP: 143 alive / 98 gold
- HTTPS: 121 alive / 41 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45104
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
