# SyndProxy validated proxy pool

## Current pool

- Alive now: 677
- Gold now: 400
- HTTP: 142 alive / 79 gold
- HTTPS: 189 alive / 22 gold
- SOCKS4: 171 alive / 146 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39958
- Ever gold: 1304

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
