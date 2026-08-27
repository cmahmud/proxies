# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 399
- HTTP: 91 alive / 52 gold
- HTTPS: 51 alive / 21 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41696
- Ever gold: 1342

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
