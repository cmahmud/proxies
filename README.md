# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 417
- HTTP: 347 alive / 91 gold
- HTTPS: 219 alive / 28 gold
- SOCKS4: 228 alive / 144 gold
- SOCKS5: 248 alive / 154 gold

## Historical pool

- Discovered: 164927
- Ever alive: 32164
- Ever gold: 1171

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
