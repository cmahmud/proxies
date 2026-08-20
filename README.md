# SyndProxy private pool

## Current pool

- Alive now: 1831
- Gold now: 690
- HTTP: 692 alive / 236 gold
- HTTPS: 592 alive / 147 gold
- SOCKS4: 221 alive / 143 gold
- SOCKS5: 326 alive / 164 gold

## Historical pool

- Discovered: 142715
- Ever alive: 24482
- Ever gold: 1026

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
