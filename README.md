# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 472
- HTTP: 137 alive / 94 gold
- HTTPS: 114 alive / 42 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 201 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45042
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
