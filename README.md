# SyndProxy private pool

## Current pool

- Alive now: 1163
- Gold now: 405
- HTTP: 393 alive / 93 gold
- HTTPS: 240 alive / 15 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 301 alive / 149 gold

## Historical pool

- Discovered: 131842
- Ever alive: 21218
- Ever gold: 879

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
