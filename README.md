# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 402
- HTTP: 88 alive / 60 gold
- HTTPS: 77 alive / 18 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 190 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38465
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
