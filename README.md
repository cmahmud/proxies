# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 411
- HTTP: 104 alive / 65 gold
- HTTPS: 80 alive / 20 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37078
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
