# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 530
- HTTP: 412 alive / 160 gold
- HTTPS: 246 alive / 88 gold
- SOCKS4: 232 alive / 153 gold
- SOCKS5: 200 alive / 129 gold

## Historical pool

- Discovered: 119819
- Ever alive: 18191
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
