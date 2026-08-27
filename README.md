# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 409
- HTTP: 93 alive / 60 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 178 alive / 165 gold
- SOCKS5: 191 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41545
- Ever gold: 1337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
