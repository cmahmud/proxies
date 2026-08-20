# SyndProxy private pool

## Current pool

- Alive now: 640
- Gold now: 386
- HTTP: 154 alive / 64 gold
- HTTPS: 73 alive / 14 gold
- SOCKS4: 203 alive / 153 gold
- SOCKS5: 210 alive / 155 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25718
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
