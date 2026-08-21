# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 443
- HTTP: 367 alive / 111 gold
- HTTPS: 264 alive / 34 gold
- SOCKS4: 193 alive / 143 gold
- SOCKS5: 266 alive / 155 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28648
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
