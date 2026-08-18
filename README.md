# SyndProxy private pool

## Current pool

- Alive now: 765
- Gold now: 253
- HTTP: 223 alive / 29 gold
- HTTPS: 143 alive / 8 gold
- SOCKS4: 213 alive / 136 gold
- SOCKS5: 186 alive / 80 gold

## Historical pool

- Discovered: 94344
- Ever alive: 9679
- Ever gold: 373

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
