# SyndProxy private pool

## Current pool

- Alive now: 1279
- Gold now: 545
- HTTP: 468 alive / 176 gold
- HTTPS: 346 alive / 71 gold
- SOCKS4: 231 alive / 140 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19570
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
