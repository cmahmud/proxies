# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 440
- HTTP: 96 alive / 68 gold
- HTTPS: 92 alive / 32 gold
- SOCKS4: 170 alive / 163 gold
- SOCKS5: 187 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47453
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
