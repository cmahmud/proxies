# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 412
- HTTP: 184 alive / 80 gold
- HTTPS: 160 alive / 23 gold
- SOCKS4: 212 alive / 155 gold
- SOCKS5: 230 alive / 154 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26965
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
