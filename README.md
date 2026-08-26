# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 400
- HTTP: 92 alive / 59 gold
- HTTPS: 83 alive / 14 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39159
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
