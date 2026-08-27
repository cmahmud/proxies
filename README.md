# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 414
- HTTP: 113 alive / 65 gold
- HTTPS: 136 alive / 19 gold
- SOCKS4: 177 alive / 164 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41352
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
