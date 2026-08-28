# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 407
- HTTP: 86 alive / 61 gold
- HTTPS: 105 alive / 24 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42978
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
