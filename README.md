# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 402
- HTTP: 92 alive / 58 gold
- HTTPS: 72 alive / 15 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 191 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39168
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
