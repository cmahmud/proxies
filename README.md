# SyndProxy validated proxy pool

## Current pool

- Alive now: 470
- Gold now: 350
- HTTP: 110 alive / 42 gold
- HTTPS: 39 alive / 9 gold
- SOCKS4: 158 alive / 155 gold
- SOCKS5: 163 alive / 144 gold

## Historical pool

- Discovered: 171087
- Ever alive: 32860
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
