# SyndProxy private pool

## Current pool

- Alive now: 1221
- Gold now: 592
- HTTP: 440 alive / 178 gold
- HTTPS: 325 alive / 109 gold
- SOCKS4: 226 alive / 145 gold
- SOCKS5: 230 alive / 160 gold

## Historical pool

- Discovered: 125594
- Ever alive: 19565
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
