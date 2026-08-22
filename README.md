# SyndProxy private pool

## Current pool

- Alive now: 740
- Gold now: 409
- HTTP: 189 alive / 89 gold
- HTTPS: 144 alive / 26 gold
- SOCKS4: 191 alive / 138 gold
- SOCKS5: 216 alive / 156 gold

## Historical pool

- Discovered: 162443
- Ever alive: 31442
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
