# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 473
- HTTP: 139 alive / 96 gold
- HTTPS: 121 alive / 42 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 202 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45046
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
