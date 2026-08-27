# SyndProxy validated proxy pool

## Current pool

- Alive now: 656
- Gold now: 406
- HTTP: 111 alive / 61 gold
- HTTPS: 176 alive / 16 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 196 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40739
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
