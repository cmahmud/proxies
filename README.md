# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 414
- HTTP: 97 alive / 70 gold
- HTTPS: 81 alive / 20 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 174 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41756
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
