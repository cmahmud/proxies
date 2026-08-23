# SyndProxy validated proxy pool

## Current pool

- Alive now: 530
- Gold now: 365
- HTTP: 109 alive / 39 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 195 alive / 158 gold

## Historical pool

- Discovered: 171593
- Ever alive: 32935
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
