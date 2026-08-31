# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 456
- HTTP: 115 alive / 89 gold
- HTTPS: 122 alive / 33 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45656
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
