# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 404
- HTTP: 93 alive / 59 gold
- HTTPS: 76 alive / 20 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41734
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
