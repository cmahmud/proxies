# SyndProxy private pool

## Current pool

- Alive now: 722
- Gold now: 362
- HTTP: 183 alive / 67 gold
- HTTPS: 153 alive / 19 gold
- SOCKS4: 193 alive / 133 gold
- SOCKS5: 193 alive / 143 gold

## Historical pool

- Discovered: 149497
- Ever alive: 26657
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
