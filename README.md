# SyndProxy validated proxy pool

## Current pool

- Alive now: 610
- Gold now: 412
- HTTP: 109 alive / 65 gold
- HTTPS: 138 alive / 19 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 186 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41351
- Ever gold: 1326

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
