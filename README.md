# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 359
- HTTP: 71 alive / 52 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 166 alive / 137 gold
- SOCKS5: 176 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42857
- Ever gold: 1364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
