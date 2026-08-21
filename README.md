# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 337
- HTTP: 236 alive / 90 gold
- HTTPS: 173 alive / 19 gold
- SOCKS4: 189 alive / 129 gold
- SOCKS5: 193 alive / 99 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28945
- Ever gold: 1116

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
