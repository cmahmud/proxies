# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 384
- HTTP: 307 alive / 87 gold
- HTTPS: 221 alive / 23 gold
- SOCKS4: 160 alive / 107 gold
- SOCKS5: 241 alive / 167 gold

## Historical pool

- Discovered: 166622
- Ever alive: 32456
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
