# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 365
- HTTP: 216 alive / 76 gold
- HTTPS: 152 alive / 22 gold
- SOCKS4: 197 alive / 132 gold
- SOCKS5: 237 alive / 135 gold

## Historical pool

- Discovered: 156840
- Ever alive: 29645
- Ever gold: 1134

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
