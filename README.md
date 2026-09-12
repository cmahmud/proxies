# SyndProxy validated proxy pool

## Current pool

- Alive now: 398
- Gold now: 332
- HTTP: 83 alive / 65 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 132 alive / 116 gold
- SOCKS5: 147 alive / 134 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49549
- Ever gold: 1586

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
