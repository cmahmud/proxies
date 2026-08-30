# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 461
- HTTP: 126 alive / 94 gold
- HTTPS: 122 alive / 37 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 202 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44829
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
