# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 420
- HTTP: 99 alive / 72 gold
- HTTPS: 109 alive / 24 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 177 alive / 163 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41806
- Ever gold: 1343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
