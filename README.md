# SyndProxy validated proxy pool

## Current pool

- Alive now: 638
- Gold now: 399
- HTTP: 103 alive / 59 gold
- HTTPS: 166 alive / 15 gold
- SOCKS4: 175 alive / 157 gold
- SOCKS5: 194 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40725
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
