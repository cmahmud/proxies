# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 283
- HTTP: 350 alive / 28 gold
- HTTPS: 183 alive / 4 gold
- SOCKS4: 228 alive / 134 gold
- SOCKS5: 244 alive / 117 gold

## Historical pool

- Discovered: 102805
- Ever alive: 12715
- Ever gold: 399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
