# SyndProxy private pool

## Current pool

- Alive now: 715
- Gold now: 247
- HTTP: 188 alive / 27 gold
- HTTPS: 93 alive / 6 gold
- SOCKS4: 223 alive / 122 gold
- SOCKS5: 211 alive / 92 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
