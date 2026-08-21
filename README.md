# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 407
- HTTP: 275 alive / 82 gold
- HTTPS: 164 alive / 21 gold
- SOCKS4: 242 alive / 161 gold
- SOCKS5: 239 alive / 143 gold

## Historical pool

- Discovered: 156825
- Ever alive: 29618
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
