# SyndProxy validated proxy pool

## Current pool

- Alive now: 629
- Gold now: 483
- HTTP: 143 alive / 99 gold
- HTTPS: 119 alive / 45 gold
- SOCKS4: 178 alive / 164 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45101
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
