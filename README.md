# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 592
- HTTP: 437 alive / 177 gold
- HTTPS: 324 alive / 109 gold
- SOCKS4: 227 alive / 144 gold
- SOCKS5: 228 alive / 162 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19566
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
