# SyndProxy private pool

## Current pool

- Alive now: 774
- Gold now: 403
- HTTP: 193 alive / 85 gold
- HTTPS: 154 alive / 23 gold
- SOCKS4: 197 alive / 144 gold
- SOCKS5: 230 alive / 151 gold

## Historical pool

- Discovered: 151071
- Ever alive: 27417
- Ever gold: 1096

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
