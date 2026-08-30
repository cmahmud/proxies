# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 445
- HTTP: 101 alive / 84 gold
- HTTPS: 53 alive / 29 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43682
- Ever gold: 1377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
