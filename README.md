# SyndProxy private pool

## Current pool

- Alive now: 1673
- Gold now: 637
- HTTP: 718 alive / 238 gold
- HTTPS: 532 alive / 133 gold
- SOCKS4: 186 alive / 101 gold
- SOCKS5: 237 alive / 165 gold

## Historical pool

- Discovered: 143424
- Ever alive: 24688
- Ever gold: 1032

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
