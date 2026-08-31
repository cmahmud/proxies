# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 478
- HTTP: 146 alive / 104 gold
- HTTPS: 115 alive / 38 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45088
- Ever gold: 1423

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
