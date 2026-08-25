# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 424
- HTTP: 130 alive / 72 gold
- HTTPS: 87 alive / 23 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35130
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
