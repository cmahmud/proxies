# SyndProxy private pool

## Current pool

- Alive now: 1275
- Gold now: 598
- HTTP: 481 alive / 180 gold
- HTTPS: 340 alive / 113 gold
- SOCKS4: 223 alive / 144 gold
- SOCKS5: 231 alive / 161 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19569
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
