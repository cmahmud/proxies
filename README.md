# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 405
- HTTP: 108 alive / 62 gold
- HTTPS: 171 alive / 16 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40748
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
