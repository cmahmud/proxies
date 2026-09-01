# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 466
- HTTP: 141 alive / 93 gold
- HTTPS: 124 alive / 38 gold
- SOCKS4: 171 alive / 163 gold
- SOCKS5: 187 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46897
- Ever gold: 1456

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
