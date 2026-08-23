# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 350
- HTTP: 145 alive / 40 gold
- HTTPS: 52 alive / 9 gold
- SOCKS4: 196 alive / 155 gold
- SOCKS5: 224 alive / 146 gold

## Historical pool

- Discovered: 171094
- Ever alive: 32875
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
