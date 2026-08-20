# SyndProxy private pool

## Current pool

- Alive now: 1512
- Gold now: 573
- HTTP: 621 alive / 197 gold
- HTTPS: 446 alive / 96 gold
- SOCKS4: 225 alive / 144 gold
- SOCKS5: 220 alive / 136 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22828
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
